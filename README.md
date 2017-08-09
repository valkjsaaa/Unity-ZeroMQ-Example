An example of Unity 3D 2017 works with ZeroMQ
=============================================

### Environment

Unity 2017.1
Python 3.6.0

Tested on macOS Sierra

### What's in this demo

Python scripts:

- [server](Python/server.py) (in a PUB/SUB model)
- [client](Python/client.py) (in a REQ/REP model)

C# scripts:

- [client](Assets/ClientObject.cs) (in a PUB/SUB model)
- [server](Assets/ServerObject.cs) (in a REQ/REP model)

Scene:

- [Main demo scene](Assets/main.unity)

### How to run

First start 2 python scripts (in seperate shell sessions):

```bash
./Python/server.py
./Python/client.py
```

Then start play mode of main demo scene in Unity Editor.

You should see the box jump around according to commands sent by python server script and python client script should be able to receive the location update of the same box.
