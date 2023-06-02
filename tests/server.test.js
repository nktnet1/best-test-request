import request from "sync-request";

const SYNC_REQUEST = process.env.SYNC_REQUEST;
const GET_REQUEST = process.env.GET_REQUEST;

if (SYNC_REQUEST) {
  if (GET_REQUEST) {
    for (let i = 0; i < 1000; i++) {
      test(`sync-request GET ${i}`, () => {
        const response = request(
          'GET',
          'http://127.0.0.1:5001/',
          {
            qs: { input: i },
          },
        );
        expect(
          JSON.parse(response.getBody('utf-8')).output
        ).toStrictEqual(i * 2);
      });
    }
  } else {
    for (let i = 0; i < 1000; i++) {
      test(`sync-request POST ${i}`, () => {
        const response = request(
          'POST',
          'http://127.0.0.1:5001/',
          {
            json: { input: i },
          },
        );
        expect(
          JSON.parse(response.getBody('utf-8')).output
        ).toStrictEqual(i * 2);
      });
    }
  }
} else {
  if (GET_REQUEST) {
    for (let i = 0; i < 1000; i++) {
      test(`fetch GET ${i}`, async () => {
        const response = await fetch(
          `http://127.0.0.1:5001?input=${i}`,
          {
            method: 'GET',
          },
        );
        const json = await response.json();
        expect(json.output).toStrictEqual(i * 2);
      });
    }
  } else {
    for (let i = 0; i < 1000; i++) {
      test(`fetch POST ${i}`, async () => {
        const response = await fetch(
          `http://127.0.0.1:5001`,
          {
            method: 'POST',
            body: JSON.stringify({ input: i }),
            headers: { 'Content-Type': 'application/json' },
          },
        );
        const json = await response.json();
        expect(json.output).toStrictEqual(i * 2);
      });
    }
  }
}
