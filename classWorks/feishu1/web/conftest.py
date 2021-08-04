import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    path_path = os.path.dirname(os.getcwd()) + "\\result\\"
    video_name = path_path + 'record.mp4'
    cmd = f"scrcpy -Nr {video_name}"
    p = subprocess.Popen(cmd, shell=True)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)