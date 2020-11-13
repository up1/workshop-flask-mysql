FROM node as builder
WORKDIR /src
COPY ./hello/package*.json ./
RUN npm install

COPY ./hello/ ./
RUN npm run build --prod

FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder ./src/build /usr/share/nginx/html 