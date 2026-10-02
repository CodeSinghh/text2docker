from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Text2Docker")

class DockerfileRequest(BaseModel):
    python_version: str = "3.11-slim"
    workdir: str = "/app"
    has_requirements: bool = True
    start_command: str = "python app.py"
    exposed_port: str = ""

@app.post("/api/generate")
def generate_dockerfile(req: DockerfileRequest):
    lines = [
        f"FROM python:{req.python_version.strip()}",
        f"WORKDIR {req.workdir.strip()}",
        ""
    ]

    if req.has_requirements:
        lines.extend([
            "COPY requirements.txt .",
            "RUN pip install --no-cache-dir -r requirements.txt",
            ""
        ])

    lines.extend([
        "COPY . .",
        ""
    ])

    if req.exposed_port.strip():
        lines.extend([
            f"EXPOSE {req.exposed_port.strip()}",
            ""
        ])

    cmd_parts = req.start_command.strip().split()
    cmd_formatted = ", ".join(f'"{part}"' for part in cmd_parts)
    lines.append(f"CMD [{cmd_formatted}]")

    return {"dockerfile": "\n".join(lines)}
