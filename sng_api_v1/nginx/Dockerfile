FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

# RUN rm /etc/nginx/conf.d/examplessl.conf

# Copy config
COPY nginx.conf /etc/nginx

# Define working directory
WORKDIR /etc/nginx

# Define default command
CMD ["nginx"]