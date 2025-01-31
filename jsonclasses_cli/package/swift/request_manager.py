def request_manager(base_url: str, use_session: bool) -> str:
    return f"""
struct RequestManager {'{'}

    static let shared = RequestManager()

    let baseURL: String = "{base_url}"

    func qs<T: Codable>(_ query: T? = nil) -> String {'{'}
        if let query = query {'{'}
            return "?" + (try! QSEncoder().encode(query))
        {'}'} else {'{'}
            return ""
        {'}'}
    {'}'}

    func url<T: Codable>(url: String, query: T) -> URL {'{'}
        return URL(string: baseURL + url + qs(query))!
    {'}'}

    func request<T: Codable, U: Codable, V: Codable>(
        method: String,
        url: String,
        input: T? = nil,
        query: U? = nil
    ) async throws -> V? {'{'}
        let url = self.url(url: url, query: query)
        var request = URLRequest(url: url)
        request.httpMethod = method
        if let input = input {'{'}
            request.httpBody = try! JSONEncoder().encode(input)
        {'}'}{_session_setter() if use_session else ''}
        let (data, response) = try await URLSession.shared.data(for: request)
        if let response = response as? HTTPURLResponse {'{'}
            if response.statusCode == 200 {'{'}
                let responseObject = try! JSONDecoder().decode(Response<V>.self, from: data)
                return responseObject.data
            {'}'} else {'{'}
                return nil
            {'}'}
        {'}'} else {'{'}
            return nil
        {'}'}
    {'}'}

    func post<T: Codable, U: Codable, V: Codable>(
        url: String,
        input: T,
        query: U? = nil
    ) async throws -> V {'{'}
        return try await request(method: "POST", url: url, input: input, query: query)!
    {'}'}

    func patch<T: Codable, U: Codable, V: Codable>(
        url: String,
        input: T,
        query: U? = nil
    ) async throws -> V {'{'}
        return try await request(method: "PATCH", url: url, input: input, query: query)!
    {'}'}

    func delete<T: Codable, U: Codable, V: Codable>(
        url: String,
        input: T? = nil,
        query: U? = nil
    ) async throws -> V? {'{'}
        try await request(method: "DELETE", url: url, input: input, query: query)
    {'}'}

    func get<T: Codable, U: Codable, V: Codable>(
        url: String,
        input: T? = nil,
        query: U? = nil
    ) async throws -> V? {'{'}
        return try await request(method: "PATCH", url: url, input: input, query: query)!
    {'}'}
{'}'}

    """.strip() + '\n'


def _session_setter() -> str:
    return '\n' + """
        if let session = SessionManager.shared.session {
            request.setValue("Bearer \(session.token)", forHTTPHeaderField: "Authorization")
        }""".strip('\n')
