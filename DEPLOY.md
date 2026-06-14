# Deploying to GitHub Pages

This project is a Vite + React SPA. The steps below publish it to GitHub
Pages using the [`gh-pages`](https://www.npmjs.com/package/gh-pages) npm
package, which pushes the built `dist/` folder to a `gh-pages` branch.

## 1. Push the project to GitHub

If this folder isn't a git repo yet:

```bash
git init
git add .
git commit -m "Initial commit"
```

Create a new repository on GitHub (e.g. `python-bootcamp-site`), then:

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

## 2. Install gh-pages

```bash
npm install -D gh-pages
```

## 3. Set the Vite base path

GitHub Pages serves project sites from `https://<username>.github.io/<repo>/`,
so Vite needs to know the site lives in a subpath. Edit
`vite.config.js`:

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/<your-repo>/',
})
```

Replace `<your-repo>` with the exact repository name (case-sensitive).

## 4. Add deploy scripts to package.json

Add these two scripts:

```json
{
  "scripts": {
    "predeploy": "npm run build",
    "deploy": "gh-pages -d dist"
  }
}
```

## 5. Fix client-side routing (React Router)

GitHub Pages has no server-side rewrites, so a hard refresh or direct link to
a route like `/quick-reference` will 404. The standard SPA fix is to copy
`index.html` to `404.html` after every build so GitHub Pages falls back to
the app for unknown paths.

Update the `predeploy` script to do this automatically:

```json
{
  "scripts": {
    "predeploy": "npm run build && cp dist/index.html dist/404.html",
    "deploy": "gh-pages -d dist"
  }
}
```

## 6. Deploy

```bash
npm run deploy
```

This builds the app and pushes `dist/` to the `gh-pages` branch of your
repo.

## 7. Enable GitHub Pages

On GitHub: go to **Settings → Pages**, set:
- **Source**: `Deploy from a branch`
- **Branch**: `gh-pages` / `/ (root)`

Save. Your site will be live at:

```
https://<your-username>.github.io/<your-repo>/
```

(it may take a minute or two to go live after the first deploy)

## 8. Redeploying after changes

Whenever you make changes:

```bash
git add .
git commit -m "Update content"
git push
npm run deploy
```

`npm run deploy` rebuilds and re-publishes `dist/` — it doesn't require a
separate GitHub Actions setup.
