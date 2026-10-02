<div align="center">

  <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" alt="Text2Docker Logo" width="100" height="100">

  # Text2Docker

  **Automated, production-ready Dockerfile generation for Python applications.**

  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
  [![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

  [Live Demo](https://text2docker.vercel.app) • [Report Bug](https://github.com/YOUR_USERNAME/text2docker/issues) • [Request Feature](https://github.com/YOUR_USERNAME/text2docker/issues)

</div>

---

## 📸 Preview

<div align="center">
  <img src="https://via.placeholder.com/1200x630/0f172a/f8fafc?text=Text2Docker+-+Liquid+Glass+UI+Preview" alt="Text2Docker App UI Preview" width="100%">
  <p><em>Minimal Liquid Glass UI running on Tailwind CSS and FastAPI serverless functions.</em></p>
</div>

---

## ✨ Features

- ⚡ **Instant Code Generation:** Get clean Dockerfiles without writing repetitive syntax manually.
- 🎨 **Liquid Glass Aesthetics:** Designed with translucent frosted elements, soft blurs, and Apple-inspired visuals.
- 🛡️ **Layer Optimization:** Automatically separates dependency installations (`requirements.txt`) from application code for efficient Docker caching.
- 🚀 **Serverless Native:** Zero runtime overhead, deployed using serverless FastAPI on Vercel.
- 📋 **One-Click Copy:** Instant clipboard integration to easily paste directly into your projects.

---

## 🏗️ Architecture

```text
┌──────────────────────────┐         POST /api/generate         ┌──────────────────────────┐
│                          │ ─────────────────────────────────> │                          │
│   Tailwind Glass UI      │                                    │   FastAPI Engine         │
│   (Vercel Edge/Public)   │ <───────────────────────────────── │   (Serverless Function)  │
│                          │          JSON Dockerfile           │                          │
└──────────────────────────┘                                    └──────────────────────────┘
