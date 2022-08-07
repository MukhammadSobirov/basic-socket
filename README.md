## Socker Programming with Python

### Steps
1. set up a separate environment
    ```bash
        python3 -m venv env
    ```

2. activate env
    ```bash
        source env/bin/activate
    ```


### Binding the Socket

```py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 3000
    hostname = '127.0.0.1'
    s.bind((hostname, port))
```


