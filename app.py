from flask import Flask, render_template, request
import os
import glob

app = Flask(__name__)


@app.route('/')
def video_list():  # put application's code here
    dir = 'static'
    files = glob.glob(os.path.join(dir, '*.mkv'))
    print(files)
    grid = 3
    # data = [files[i:i + grid] for i in range(0, len(files), grid)]
    return render_template('video_list.html', data=files)


@app.route('/video')
def video():  # put application's code here
    video = request.args.get("video")
    return render_template('video.html', video=video)


if __name__ == '__main__':
    app.run(debug=True)
