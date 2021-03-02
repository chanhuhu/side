import React from "react";
import "./Card.css";

type Props = {
  children: React.ReactNode;
} & React.DetailedHTMLProps<
  React.HTMLAttributes<HTMLDivElement>,
  HTMLDivElement
>;

export default function Card({ children, ...props }: Props) {
  return (
    <div className="card" {...props}>
      {children}
    </div>
  );
}
