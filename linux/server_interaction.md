# Useful commands to interact with the server

Install and (re)start the service:
```
systemctl restart ci-server.service
```

To check the status:
```
systemctl status ci-server
```

To check the runtime behaviour:
```
journalctl -f
```