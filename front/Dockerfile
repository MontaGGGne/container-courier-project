FROM node:20-alpine


WORKDIR /workdir
COPY ./front/* /workdir/

# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install npm -y
RUN npm install
# RUN npx expo start
EXPOSE 80
RUN ls
# CMD ["npm", "run", "reset-project"]