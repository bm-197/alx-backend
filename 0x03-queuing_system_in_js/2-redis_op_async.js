#!/usr/bin/yarn dev
import promisify from 'utils'
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client connected to server:', err.toString());
});

const setNewShool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const get = promisfy(client.GET).bind(client);

const displaySchoolValue = async (schoolName) => {
  console.log(await get(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}


client.on('connect', async () => {
  console.log('Redis client not connected to server');
  await main();
});

