import typer as typer
import uvicorn as uvicorn

app = typer.Typer()


@app.command()
def run(workers: int = 1):
    uvicorn.run(
        "src.framework.application:app", port=8000, host="0.0.0.0", workers=workers, app_dir="src", log_config=None
    )


if __name__ == "__main__":
    app()
