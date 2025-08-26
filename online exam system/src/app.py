from flask import Flask, request, jsonify
import subprocess
import threading

app = Flask(__name__)

@app.route('/enable-eye-tracking', methods=['POST'])
def enable_eye_tracking():
    try:
        # Run your Python script in a separate thread to avoid blocking the server
        eye_tracking_thread = threading.Thread(target=run_eye_tracking_script)
        eye_tracking_thread.start()

        return jsonify({'success': True, 'message': 'Eye tracking enabled successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
@app.route('/enable-speech-detector', methods=['POST'])
def enable_speech_detector():
    try:
        # Run your speech detection script in a separate thread to avoid blocking the server
        speech_detection_thread = threading.Thread(target=run_speech_detector_script)
        speech_detection_thread.start()

        return jsonify({'success': True, 'message': 'Speech detection enabled successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

def run_eye_tracking_script():
    # Replace the path with the actual path to your Python script
    script_path = 'C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\eye_tracking.py'
    subprocess.run(['python', script_path])

def run_speech_detector_script(): 
    # Replace the path with the actual path to your speech detection Python script
    speech_detection_script_path = 'C:\\Vivek Chauhan\\Python\\vision_voice_navigator\\test.py'
    subprocess.run(['python', speech_detection_script_path])

if __name__ == '__main__':
    app.run(debug=True)
