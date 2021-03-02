export class Config {
  env: string;

  constructor() {
    this.env = process.env.NODE_ENV!;
  }
}
