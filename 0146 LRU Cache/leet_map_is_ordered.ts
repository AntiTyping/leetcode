class LRUCache {
  private readonly cache = new Map<number, number>();

  constructor(private readonly capacity: number) {}

  get(key: number): number {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key)!;
    this.cache.delete(key);
    this.cache.set(key, value); // re-insert => now newest
    return value;
  }

  put(key: number, value: number): void {
    this.cache.delete(key);
    if (this.cache.size === this.capacity) {
      this.cache.delete(this.cache.keys().next().value!);
    }
    this.cache.set(key, value);
  }
}