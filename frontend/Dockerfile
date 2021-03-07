FROM 476258813568.dkr.ecr.us-east-1.amazonaws.com/node:14.5.5-alpine3.13

WORKDIR /usr/src/code

# Copy and install yarn dependencies
COPY ./frontend/package.json ./frontend/yarn.lock ./frontend/webpack.config.js ./frontend/.babelrc ./
RUN yarn install

# Copy app and static files
COPY ./bud_band/static ./bud_band/static

RUN yarn run deploy
