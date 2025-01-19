import { SummaryResponse } from "../interfaces/SummaryResponse";

interface Props {
  response: SummaryResponse;
}

const SummaryTable = ({
  response: { details, skill_level, experience_level, score },
}: Props) => {
  return (
    <table className="text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
      <thead>
        <tr className="bg-gray-100">
          <th className="border border-gray-300 px-4 py-2">Type</th>
          <th className="border border-gray-300 px-4 py-2">Values</th>
        </tr>
      </thead>
      <tbody>
        {details.full_name && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Full Name</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.full_name[0]}
            </td>
          </tr>
        )}
        {details.email && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Email</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.email[0]}
            </td>
          </tr>
        )}
        {details.phone_number && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Phone number</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.phone_number[0]}
            </td>
          </tr>
        )}
        {details.tech_stacks && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Tool(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.tech_stacks.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < details.tech_stacks!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {details.experience && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Project(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              Worked on{" "}
              {details.experience.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < details.experience!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {details.institute && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">School(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.institute.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < details.institute!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {details.languages_spoken && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Languages(s)</td>
            <td className="border border-gray-300 px-4 py-2">
              {details.languages_spoken.map((name, index) => (
                <span key={index}>
                  {name}
                  {index < details.languages_spoken!.length - 1 && ", "}
                </span>
              ))}
            </td>
          </tr>
        )}
        {experience_level && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Level</td>
            <td className="border border-gray-300 px-4 py-2">
              {experience_level}
            </td>
          </tr>
        )}
        {skill_level && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Skill</td>
            <td className="border border-gray-300 px-4 py-2">{skill_level}</td>
          </tr>
        )}
        {score && (
          <tr>
            <td className="border border-gray-300 px-4 py-2">Score</td>
            <td className="border border-gray-300 px-4 py-2">{score}</td>
          </tr>
        )}
      </tbody>
    </table>
  );
};

export default SummaryTable;
