#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = creatClient();

client.on('error', (err) => {
  console.log('Redis client not connected to server:', err.toString());
});

const publicMessage = (message, time) => {
  setTimeout(() => {
      conole.log(`About to send ${message}`);
      client.publish('holberton school channel', message);
  }, time);
}

client.on('connect', () => {
  console.log('Redis client connected to server');
});

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 200);
publishMessage('Holberton Student #3 starts course', 400);

