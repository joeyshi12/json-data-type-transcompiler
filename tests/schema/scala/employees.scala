import org.joda.time.DateTime

case class Root(
    employees: IndexedSeq[employeesItem]
)

case class employeesItem(
    firstName: String,
    lastName: String
)
