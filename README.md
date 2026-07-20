# Seiso Smart Router

Not serving inference on this. Just keeping it open source since part of the project orginally. Seems like alot of unknown 

Standalone Smart Router service extracted from SeisoLocalAI.

This repo contains the router server, Nemotron-Orchestrator-8B routing path,
LiteLLM/vLLM dispatch, llama-swap backend lifecycle configs, deployment files,
and router-specific tests.

The Forge app integration remains in SeisoLocalAI:

- `forge/services/model_router_client.py`
- Forge inference routes and orchestrator hooks
- `ROUTER_MODEL_ID` / Smart Router model option
- frontend Chat UI router status and model-picker behavior

That boundary keeps local Forge inference functional while allowing this router
service to live and evolve separately.

## Run Locally

Install the service:

```bash
pip install -e ".[dev]"
```

Start the default llama.cpp router:

```bash
seiso-router serve --config deploy/model-router/config/router.local.yaml
```

Start the vLLM/Nemotron Docker stack:

```bash
./start-router-vllm
```

Then enable Forge in SeisoLocalAI with:

```bash
SEISO_MODEL_ROUTER_ENABLED=true
SEISO_MODEL_ROUTER_URL=http://127.0.0.1:8780
```

Detailed router deployment notes are in
[deploy/model-router/README.md](deploy/model-router/README.md).

