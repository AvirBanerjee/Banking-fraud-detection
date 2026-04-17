import { useState } from "react";
import TransactionForm from "../components/TransactionForm";
import ResultCard from "../components/ResultCard";

export default function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6 flex flex-col items-center gap-6">
      <h1 className="text-3xl font-bold text-blue-700">
        Banking Fraud Detection System
      </h1>

      <div className="grid md:grid-cols-2 gap-6 w-full max-w-4xl">
        <TransactionForm setResult={setResult} />
        <ResultCard result={result} />
      </div>
    </div>
  );
}