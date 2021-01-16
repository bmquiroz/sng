# Build Angular app
FROM node:latest as node

# RUN npm config set proxy http://username:password@host:port
# RUN npm config set https-proxy http://username:password@host:port

WORKDIR /app
# COPY package.json ./
COPY . .
RUN npm install
RUN npm run build --prod

# Deploy SPA app
FROM nginx:alpine
COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=node /app/dist/sng-app /usr/share/nginx/html
ENTRYPOINT ["nginx", "-g", "daemon off;"]