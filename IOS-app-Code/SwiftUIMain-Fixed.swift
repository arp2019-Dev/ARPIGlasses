//
//  SwiftUIView.swift
//  ArpiGlasses
//
//  Created by Akhil Raju on 6/17/25.
//

import SwiftUI
import Vision
import AVFoundation
import ARKit
import Speech
import Network

struct ContentView: View {
    @StateObject var viewModel = ARViewModel()

    var body: some View {
        VStack {
            if let image = viewModel.latestImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 300)
                    .onTapGesture { location in
                        viewModel.sendAnnotation(at: location)
                    }
            }

            Picker("Mode", selection: $viewModel.mode) {
                Text("Detection").tag("detection")
                Text("Text").tag("text")
                Text("Draw").tag("draw")
            }
            .pickerStyle(SegmentedPickerStyle())
            .padding()

            Button("Start Voice Input") {
                viewModel.startSpeech()
            }
        }
        .onAppear {
            viewModel.connectWebSocket()
            viewModel.startARTracking()
            viewModel.fetchFrames()
        }
    }
}

class ARViewModel: NSObject, ObservableObject, SFSpeechRecognizerDelegate, ARSessionDelegate {
    @Published var latestImage: UIImage?
    @Published var mode: String = "detection" {
        didSet { sendMode() }
    }

    private var connection: NWConnection?
    private let speechRecognizer = SFSpeechRecognizer()
    private let audioEngine = AVAudioEngine()
    private var arSession = ARSession()

    func connectWebSocket() {
        let host = NWEndpoint.Host(" IP I dont have yet ")
        let port = NWEndpoint.Port(rawValue: 8765) ?? 8765
        connection = NWConnection(host: host, port: port, using: .tcp)
        connection?.start(queue: .global())
    }

    func startARTracking() {
        arSession.delegate = self
        arSession.run(ARWorldTrackingConfiguration())
    }

    func session(_ session: ARSession, didUpdate frame: ARFrame) {
        let pitch = frame.camera.eulerAngles.x * 180 / .pi
        let yaw = frame.camera.eulerAngles.y * 180 / .pi
        let payload: [String: Any] = ["pose": ["pitch": pitch, "yaw": yaw]]
        sendJSON(payload)
    }

    func fetchFrames() {
        Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            guard let url = URL(string: "http://IP I dont have yet/") else { return }
            URLSession.shared.dataTask(with: url) { data, _, _ in
                if let data = data, let img = UIImage(data: data) {
                    DispatchQueue.main.async { self.latestImage = img }
                    self.processImage(img)
                }
            }.resume()
        }
    }

    func processImage(_ image: UIImage) {
        guard mode == "detection", let ciImage = CIImage(image: image) else { return }
        guard let model = try? VNCoreMLModel(for: FastViTT8F16().model) else { return }

        let request = VNCoreMLRequest(model: model) { req, _ in
            guard let results = req.results as? [VNRecognizedObjectObservation] else { return }
            let boxes = results.map {
                [Int($0.boundingBox.minX * 640), Int((1 - $0.boundingBox.maxY) * 480),
                 Int($0.boundingBox.width * 640), Int($0.boundingBox.height * 480),
                 $0.labels.first?.identifier ?? "Obj"] as [Any]
            }
            self.sendJSON(["boxes": boxes])
        }
        request.imageCropAndScaleOption = .scaleFill
        try? VNImageRequestHandler(ciImage: ciImage).perform([request])
    }


    func sendAnnotation(at point: CGPoint) {
        let x = Int(point.x)
        let y = Int(point.y)
        let data: [String: Any] = ["annotate": ["x": x, "y": y, "text": "Note"]]
        sendJSON(data)
    }

    func startSpeech() {
        let node = audioEngine.inputNode
        let request = SFSpeechAudioBufferRecognitionRequest()
        let format = node.outputFormat(forBus: 0)
        node.installTap(onBus: 0, bufferSize: 1024, format: format) { buffer, _ in
            request.append(buffer)
        }
        audioEngine.prepare()
        try? audioEngine.start()
        speechRecognizer?.recognitionTask(with: request) { result, _ in
            if let result = result, result.isFinal {
                self.sendJSON(["voice": result.bestTranscription.formattedString])
            }
        }
    }

    func sendMode() {
        sendJSON(["mode": mode])
    }

    func sendJSON(_ obj: [String: Any]) {
        guard let connection = connection else { return }
        if let data = try? JSONSerialization.data(withJSONObject: obj) {
            connection.send(content: data, completion: .contentProcessed({ _ in }))
        }
    }
}
