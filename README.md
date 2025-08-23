# EIA Crush — GitHub Pages

Este repositório publica o jogo **EIA Crush** em GitHub Pages.

## Conteúdo
- `index.html` — o jogo (baseado no ficheiro fornecido)
- `404.html` — redireciona para `index.html` (útil para SPA/refresh)
- `.nojekyll` — evita processamento do Jekyll no Pages
- `LICENSE` — licença MIT

## Como publicar
1. Crie um repositório no GitHub (por ex.: `eia-crush`).
2. Faça upload destes ficheiros para a raiz do repositório.
3. Em **Settings » Pages**:
   - **Source**: *Deploy from a branch*
   - **Branch**: selecione `main` e `/ (root)`
4. Aguarde a build e abra a URL apresentada (algo como `https://<utilizador>.github.io/eia-crush/`).

### Domínio personalizado (opcional)
- Em **Settings » Pages**, adicione o domínio (ex.: `game.eia.pt`).
- Crie um registo DNS **CNAME** apontando `game.eia.pt` para `<utilizador>.github.io`.
- Opcionalmente, crie um ficheiro `CNAME` na raiz do repo com o domínio:

```
game.eia.pt
```

### Dicas
- O jogo usa CDN para Tailwind e Tone.js, por isso não requer build.
- Se pretender um workflow com GitHub Actions, pode manter as definições acima (não é necessário action).

---

© 2025 KOELHO2000 — Licenciado sob MIT.
