import uvicorn

from .settings import setting

uvicorn.run("server.app:fast_app",
            host=setting.server_host,
            port=setting.server_port)
