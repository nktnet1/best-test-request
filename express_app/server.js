import express, { json } from 'express';
import morgan from 'morgan';


const server = express();


server.use(json());
server.use(morgan('dev'));


server.post('/', (req, res) => {
  const { input } = req.body;
  res.send({ output: input * 2 });
});

server.get('/', (req, res) => {
  const { input } = req.query;
  res.send({ output: parseInt(input) * 2 });
});


export default server;
