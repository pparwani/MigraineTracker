# Use Node.js 18 Alpine as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Build the app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Run the app
CMD ["npm", "run", "dev"]