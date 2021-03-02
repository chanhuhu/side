// it's not Modern JS https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat
export default function formatTags(tags: string[]) {
  return new Intl.ListFormat("th", {
    style: "long",
    type: "conjunction",
  }).format(tags);
}
