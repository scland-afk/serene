# Serene Landscaping - Quick Deployment Guide

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

### 2. Deploy to Cloudflare Pages

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Pages**
2. Click **Create a project** → **Connect to Git**
3. Select your GitHub repository
4. Configure build settings:
   - **Build command**: `npm run build`
   - **Build output directory**: `public`
   - **Root directory**: `/` (leave empty)
   - **Node version**: `20`
5. Click **Save and Deploy**

That's it! Your site will be live in minutes.

## 📋 Build Settings Summary

- **Framework**: Eleventy (Static Site Generator)
- **Build Command**: `npm run build`
- **Output Directory**: `public`
- **Node Version**: 18 or 20

## 🔧 Local Development

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Important Files

- `.eleventy.js` - Eleventy configuration
- `package.json` - Dependencies and scripts
- `src/` - Source files (edit these)
- `public/` - Build output (auto-generated, don't edit)

## 🌐 Custom Domain

After deployment:
1. Go to your Cloudflare Pages project
2. Click **Custom domains**
3. Add your domain (e.g., `serenelandscapes.ca`)
4. Follow DNS setup instructions

## 📖 Full Documentation

See `DEPLOYMENT.md` for detailed deployment instructions.
