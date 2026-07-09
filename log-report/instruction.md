# Parse Access Log into JSON Report

An Apache-style access log is available at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json`.

## Success criteria

1. `/app/report.json` exists and contains valid JSON.
2. The JSON object has a key `total_requests` whose value is the integer count of
   log lines (one request per line; blank lines are ignored).
3. The JSON object has a key `unique_ips` whose value is the integer count of
   distinct client IP addresses (the first whitespace-delimited field on each line).
4. The JSON object has a key `top_path` whose value is the string URL path
   (e.g. `"/index.html"`) that appears most frequently as the request target across
   all log lines.

## Example output shape

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

No other keys are required. Extra keys are permitted but not checked.
