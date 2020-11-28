import p4p # No p4p import leads to seg fault 
from epicscorelibs.path import get_lib

import pcaspy
import epics
import pytest
import signal
import os
import sys
import subprocess
import time


@pytest.fixture(scope="session")
def ca_server():
    env = os.environ.copy()

    ca_proc = subprocess.Popen(
            [
                sys.executable, "run_server.py"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd= os.path.dirname(os.path.realpath(__file__)),
            env=env
    )

    # give the server a moment to start up
    time.sleep(1)

    # Check it started successfully
    assert not ca_proc.poll()

    yield ca_proc

    # teardown
    ca_proc.send_signal(signal.SIGINT)


def test_constant_variable_ca(ca_server):
    # COMMENTING OUT BELOW LEADS TO FAILED TEST, HANGING, AND ERROR MESSAGES:
    # CAC TCP socket linger set error was Invalid argument
    # CAC TCP socket shutdown error was Socket is not connected
    os.environ["PYEPICS_LIBCA"] = get_lib('ca')
    val = epics.caget("test:pv1", timeout=5.0)

    assert val == 1.0
