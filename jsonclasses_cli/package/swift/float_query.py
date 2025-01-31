def float_query():
    return """
public enum FloatQuery: Codable {
    case eq(_ value: Float)
    case gt(_ value: Float)
    case gte(_ value: Float)
    case lt(_ value: Float)
    case lte(_ value: Float)
    case or(_ values: [FloatQuery])
    case and(_ values: [FloatQuery])

    public enum CodingKeys: String, CodingKey {
        case eq = "_eq"
        case gt = "_gt"
        case gte = "_gte"
        case lt = "_lt"
        case lte = "_lte"
        case or = "_or"
        case and = "_and"
    }

    public init(from decoder: Decoder) throws {
        let container = try! decoder.container(keyedBy: CodingKeys.self)
        if container.contains(.eq) {
            self = .eq(try! container.decode(Float.self, forKey: .eq))
        } else if container.contains(.gt) {
            self = .gt(try! container.decode(Float.self, forKey: .gt))
        } else if container.contains(.gte) {
            self = .gte(try! container.decode(Float.self, forKey: .gte))
        } else if container.contains(.lt) {
            self = .lt(try! container.decode(Float.self, forKey: .lt))
        } else if container.contains(.lte) {
            self = .lte(try! container.decode(Float.self, forKey: .lte))
        } else if container.contains(.or) {
            self = .or(try! container.decode([FloatQuery].self, forKey: .or))
        } else if container.contains(.and) {
            self = .and(try! container.decode([FloatQuery].self, forKey: .and))
        } else {
            self = .eq(0)
        }
    }

    public func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        switch self {
        case .eq(let value):
            try! container.encode(value, forKey: .eq)
        case .gt(let value):
            try! container.encode(value, forKey: .gt)
        case .gte(let value):
            try! container.encode(value, forKey: .gte)
        case .lt(let value):
            try! container.encode(value, forKey: .lt)
        case .lte(let value):
            try! container.encode(value, forKey: .lte)
        case .or(let value):
            try! container.encode(value, forKey: .or)
        case .and(let value):
            try! container.encode(value, forKey: .and)
        }
    }
}
    """.strip() + "\n"
