import kue from 'kue'

const queue = kue.createQueue();

const jobData = {
    'phone': '0022990409826',
    'message': 'here is your code'
}


const job = queue.create('push_notification_code', jobData)
    .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
    });

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
