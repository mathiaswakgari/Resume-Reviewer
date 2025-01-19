import { SummaryResponse } from "../interfaces/SummaryResponse";

interface Props {
  response: SummaryResponse;
}

const SummaryTable = ({ response }: Props) => {
  return (
    <table className="text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
      <thead>
        <tr className="bg-gray-100">
          <th className="border border-gray-300 px-4 py-2">Type</th>
          <th className="border border-gray-300 px-4 py-2">Values</th>
        </tr>
      </thead>
      <tbody>
        {response.full_name && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Full Name</td>
            <td className="border border-gray-300 px-4 py-2">
              {response.full_name[0]}
            </td>
          </tr>
        )}
        {response.email && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Email</td>
            <td className="border border-gray-300 px-4 py-2">
              {response.email[0]}
            </td>
          </tr>
        )}
        {response.phone_number && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Phone number</td>
            <td className="border border-gray-300 px-4 py-2">
              {response.phone_number[0]}
            </td>
          </tr>
        )}
        {response.tech_stacks && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Tool(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              {response.tech_stacks.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < response.tech_stacks!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {response.experience && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Experience(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              Worked on{" "}
              {response.experience.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < response.experience!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {response.languages_spoken && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Languages(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              {response.languages_spoken.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < response.languages_spoken!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
      </tbody>
    </table>
  );
};

export default SummaryTable;
