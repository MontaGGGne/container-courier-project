FROM node:20-alpine


COPY ./front /workdir
WORKDIR /workdir

# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install npm -y
RUN npm install
# RUN npx expo start
EXPOSE 8081
RUN ls
CMD ["npm", "start"]