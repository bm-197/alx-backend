#!/usr/bin/yarn dev
import kue from 'kue';
const queue = kue.createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
  phoneNumber: '0900000000',
  message: 'lua',
});

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
}).on('complete', () => {
  console.log('Notification job completed')
}).on('failed attempt', () => {
  console.log('Notification job failed');
});

job.save();

