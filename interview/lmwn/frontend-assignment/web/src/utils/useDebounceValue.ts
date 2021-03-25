import { useEffect, useState } from "react";

export function useDebounceValue(value: string, timeout: number) {
  const [search, setSearch] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setSearch(value);
    }, timeout);
    return () => {
      clearTimeout(timer);
    };
  }, [value]);

  return search;
}
