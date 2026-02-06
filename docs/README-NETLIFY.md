# Netlify Deployment - Serene Landscaping

## ✅ Ready to Deploy!

This site is configured for Netlify deployment. Just connect your GitHub repository and deploy!

## 🚀 Quick Start

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 2. Deploy to Netlify

1. Go to https://app.netlify.com/
2. Click **Add new site** → **Import an existing project**
3. Choose **GitHub** and select your repository
4. Netlify will auto-detect these settings:
   - **Build command**: `npm run build`
   - **Publish directory**: `public`
5. Click **Deploy site**

That's it! Your site will be live in 2-3 minutes.

## 📋 Build Configuration

The site is pre-configured via `netlify.toml`:

- **Build command**: `npm run build`
- **Publish directory**: `public`
- **Environment**: `ELEVENTY_ENV=PROD` (set automatically)

## 🌐 Custom Domain

After deployment:
1. Go to **Site settings** → **Domain management**
2. Click **Add custom domain**
3. Enter `serenelandscapes.ca`
4. Follow DNS setup instructions

## 🔧 Local Testing

Test the build before deploying:

```bash
npm install
npm run build
ls public/index.html  # Should exist
```

## 📖 Full Documentation

See `NETLIFY-DEPLOY.md` for detailed instructions.
