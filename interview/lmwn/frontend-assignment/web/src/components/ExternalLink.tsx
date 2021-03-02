import React, { AnchorHTMLAttributes, DetailedHTMLProps } from "react";
import "./Link.css";

type Props = {
  children?: React.ReactNode;
} & DetailedHTMLProps<
  AnchorHTMLAttributes<HTMLAnchorElement>,
  HTMLAnchorElement
>;

export default function ExternalLink({ children, ...props }: Props) {
  return (
    <a className="link" {...props}>
      {children}
    </a>
  );
}
