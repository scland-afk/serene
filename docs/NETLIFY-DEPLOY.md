# Deploy to Netlify - Quick Guide

## 🚀 Quick Deployment Steps

### Option 1: Deploy via GitHub (Recommended)

1. **Push to GitHub** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

2. **Connect to Netlify**:
   - Go to https://app.netlify.com/
   - Click **Add new site** → **Import an existing project**
   - Choose **GitHub**
   - Authorize Netlify to access your repositories
   - Select your repository: `sass-serene` (or your repo name)

3. **Build Settings** (Netlify auto-detects these):
   - **Build command**: `npm run build`
   - **Publish directory**: `public`
   - **Node version**: `20` (or leave default)

4. **Environment Variables** (Optional but recommended):
   - Go to **Site settings** → **Environment variables**
   - Add: `ELEVENTY_ENV` = `PROD`
   - Click **Save**

5. **Deploy**:
   - Click **Deploy site**
   - Wait for build to complete (2-3 minutes)
   - Your site will be live at `your-site-name.netlify.app`

### Option 2: Manual Deploy (Drag & Drop)

1. **Build locally**:
   ```bash
   npm install
   npm run build
   ```

2. **Deploy**:
   - Go to https://app.netlify.com/
   - Drag and drop the `public/` folder onto Netlify
   - Your site will be live instantly!

## ✅ Build Configuration

Netlify is already configured via `netlify.toml`:

```toml
[build]
  publish = "public/"
  command = "npm run build"
```

This means Netlify will:
- Run `npm run build` to build your site
- Publish the `public/` folder
- Automatically deploy on every push to your main branch

## 🔧 Custom Domain

1. Go to **Site settings** → **Domain management**
2. Click **Add custom domain**
3. Enter your domain (e.g., `serenelandscapes.ca`)
4. Follow DNS setup instructions

## 📋 Checklist

- [ ] Code pushed to GitHub
- [ ] Netlify connected to GitHub repository
- [ ] Build command: `npm run build`
- [ ] Publish directory: `public`
- [ ] Environment variable `ELEVENTY_ENV=PROD` (optional but recommended)
- [ ] Site deployed successfully

## 🆘 Troubleshooting

### Build Fails
- Check **Deploy logs** in Netlify dashboard
- Verify `package-lock.json` is committed
- Ensure Node version is 18 or 20

### 404 Error
- Verify publish directory is `public` (not `dist` or `build`)
- Check that `public/index.html` exists after build
- Clear Netlify cache: **Deploys** → **Trigger deploy** → **Clear cache and deploy site**

### Images Not Loading
- Check image paths are correct
- Verify images are in `src/assets/images/`
- Clear browser cache

## 🎉 That's It!

Your site should be live at `your-site-name.netlify.app` within minutes!
