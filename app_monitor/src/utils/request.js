import axios from "axios";

const service = axios.create({
  baseURL: "http://8.134.127.43:8000",
  timeout: 10000,
});

// 白名单（不需要 Token 的接口）
const notoken = [
  "/api/health",
  "/health"
];

service.interceptors.request.use(
  (config) => {
    // 检查当前请求的 URL 是否在白名单中
    const isWhiteList = notoken.some(url => 
      config.url.includes(url)
    );

    // 如果不在白名单中，则添加 Token
    if (!isWhiteList) {
      const token = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918";
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
    }

    return config;
  },
  (error) => {
    // 请求错误处理
    console.error('请求错误：', error);
    return Promise.reject(error);
  }
);

export default service;