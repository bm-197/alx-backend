import kue from 'kue'

const queue = kue.createQueue();
const BLACKLISTED_NUMBER = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2, pending = 2;
  let sendInterval = setInterval(() => {
    if (total - pending <=total / 2) {
      kue.job.progress(total - pending, total);
    }
    if (BLACKLISTED_NUMBER.include(phoneNumber) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (total === pending) {
      console.log(`Sending notification to ${phoneNumber},`, `with message: ${message}`,);
    }
    --pending||done();
    pending ||clearIneterval(sendInterval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(kue.job.data.phoneNumber, kue.job.message, kue.job, done);
};

