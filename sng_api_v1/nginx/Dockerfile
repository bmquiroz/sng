FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

# RUN rm /etc/nginx/conf.d/examplessl.conf

# Copy config
COPY nginx.conf /etc/nginx
# COPY default.conf /etc/nginx/conf.d

# Define working directory
WORKDIR /etc/nginx

# Define default command
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]