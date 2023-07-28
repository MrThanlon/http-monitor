process = [
    {
        "cwd": "/home/huangziyi/developersrv",
        "url": "https://developer.canaan-creative.com/devAdmin/proj/list?pageNo=1&pageSize=1",
        "command": [
            "/data/service/jdk-17.0.2/bin/java",
            "-Dfile.encoding=UTF-8",
            "-Dserver.port=9000",
            "-jar",
            "/home/huangziyi/developersrv/developersrv-0.0.1-SNAPSHOT.jar",
            "--spring.profiles.active=prod",
            "--spring.servlet.multipart.max-file-size=2048GB",
            "--spring.servlet.multipart.max-request-size=2048GB"
        ],
    },
    {
        "cwd": "/home/huangziyi/bbs-admin-backend",
        "url": "https://developer.canaan-creative.com/bbsAdmin/external/getPostsBySort?pageNum=1&pageSize=10",
        "command": [
            "/home/huangziyi/bbs-admin-backend/main",
            "server"
        ]
    }
]
