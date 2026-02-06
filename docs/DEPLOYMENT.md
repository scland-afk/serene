# Deployment Guide for Serene Landscaping

This guide will help you deploy this site to Cloudflare Pages via GitHub.

## Prerequisites

- A GitHub account
- A Cloudflare account (free tier works)
- Node.js 18 or 20 installed locally (for testing builds)

## Step 1: Push to GitHub

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it (e.g., `serene-landscaping`)
   - Don't initialize with README, .gitignore, or license
   - Click "Create repository"

3. **Push your code**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/serene-landscaping.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Cloudflare Pages

### Option A: Automatic Deployment (Recommended)

1. **Go to Cloudflare Dashboard**:
   - Visit https://dash.cloudflare.com/
   - Navigate to **Workers & Pages** → **Pages**
   - Click **Create a project** → **Connect to Git**

2. **Connect GitHub**:
   - Select your GitHub account
   - Authorize Cloudflare to access your repositories
   - Select the `serene-landscaping` repository

3. **Configure Build Settings**:
   - **Project name**: `serene-landscaping` (or your preferred name)
   - **Production branch**: `main` (or `master`)
   - **Framework preset**: None (or Eleventy if available)
   - **Build command**: `npm run build`
   - **Build output directory**: `public`
   - **Root directory**: `/` (leave empty)
   - **Node version**: `20` (or `18`)

4. **Environment Variables** (if needed):
   - Add `ELEVENTY_ENV` = `PROD` if not automatically set

5. **Click "Save and Deploy"**

### Option B: Manual Deployment via GitHub Actions

1. **Get Cloudflare API Token**:
   - Go to https://dash.cloudflare.com/profile/api-tokens
   - Click "Create Token"
   - Use "Edit Cloudflare Workers" template
   - Add permissions: Account → Cloudflare Pages → Edit
   - Copy the token

2. **Get Account ID**:
   - Go to https://dash.cloudflare.com/
   - Select your account
   - Copy the Account ID from the right sidebar

3. **Add GitHub Secrets**:
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Add these secrets:
     - `CLOUDFLARE_API_TOKEN`: Your API token
     - `CLOUDFLARE_ACCOUNT_ID`: Your Account ID

4. **Push to trigger deployment**:
   ```bash
   git push origin main
   ```

## Step 3: Custom Domain (Optional)

1. **In Cloudflare Pages**:
   - Go to your project → **Custom domains**
   - Click **Set up a custom domain**
   - Enter your domain (e.g., `serenelandscapes.ca`)

2. **DNS Configuration**:
   - Cloudflare will provide DNS records to add
   - Add a CNAME record pointing to your Pages URL
   - Or use Cloudflare's nameservers for automatic setup

## Build Configuration

The site is configured to build with:
- **Build command**: `npm run build`
- **Output directory**: `public`
- **Node version**: 18 or 20

## Local Testing

Before deploying, test the build locally:

```bash
# Install dependencies
npm install

# Build the site
npm run build

# Preview the built site
npm run preview
```

The built site will be in the `public/` directory.

## Troubleshooting

### Build Fails
- Check Node version (should be 18 or 20)
- Ensure all dependencies are in `package.json`
- Check build logs in Cloudflare Pages dashboard

### Images Not Loading
- Verify image paths are correct
- Check that images are in `src/assets/images/`
- Ensure images are being copied to `public/` during build

### CSS Not Loading
- Verify SASS is compiling correctly
- Check that CSS files are in `public/assets/css/`
- Clear Cloudflare cache if needed

## File Structure

```
sass-serene/
├── public/          # Build output (generated, don't edit)
├── src/            # Source files
│   ├── assets/     # Images, fonts, etc.
│   ├── content/    # Pages and blog posts
│   └── _includes/  # Templates and components
├── .eleventy.js    # Eleventy configuration
├── package.json    # Dependencies and scripts
└── wrangler.toml   # Cloudflare configuration (optional)
```

## Support

For issues:
- Check Cloudflare Pages build logs
- Review GitHub Actions logs (if using Actions)
- Verify all environment variables are set correctly
