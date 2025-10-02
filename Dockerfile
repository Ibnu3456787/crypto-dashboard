# Gunakan image nginx sebagai server
FROM nginx:alpine

# Copy semua file (index.html dll) ke folder default nginx
COPY . /usr/share/nginx/html
