FROM node:20-alpine


COPY ./front /workdir
WORKDIR /workdir

RUN npm install
EXPOSE 8081
CMD ["npm", "start"]