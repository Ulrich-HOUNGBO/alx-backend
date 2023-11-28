import kue from 'kue';
import {progress} from "mocha/lib/reporters";

const jobs =  [{
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
},
    {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4153538781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4153718781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4159518782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4158718781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153818782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4154318781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4151218782',
        message: 'This is the code 4321 to verify your account'
    }
];

const queue = kue.createQueue();

for (const j of jobs) {
    const job = queue.create('push_notification', j)
        .save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        });
    job.on('complete', () => console.log(`Notification job ${job.id} completed`));
    job.on('failed', () => console.log(`Notification job ${job.id} failed`));
    job.on('progess', () => console.log(`Notification job ${job.id} ${progress}% complete`));
}