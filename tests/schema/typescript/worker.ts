export interface Root {
    PersonId: number;
    PersonNumber: string;
    CorrespondenceLanguage: CorrespondenceLanguage;
    BloodType: BloodType;
    DateOfBirth: DateOfBirth;
    DateOfDeath: DateOfDeath;
    CountryOfBirth: CountryOfBirth;
    RegionOfBirth: RegionOfBirth;
    TownOfBirth: TownOfBirth;
    ApplicantNumber: ApplicantNumber;
    CreatedBy: string;
    CreationDate: string;
    LastUpdatedBy: string;
    LastUpdateDate: string;
    workRelationships: workRelationships;
}

export interface workRelationships {
    items: itemsItem[];
}

export interface itemsItem {
    PeriodOfServiceId: number;
    LegislationCode: string;
    LegalEntityId: number;
    LegalEmployerName: LegalEmployerName;
    WorkerType: string;
    PrimaryFlag: boolean;
    StartDate: string;
    LegalEmployerSeniorityDate: LegalEmployerSeniorityDate;
    EnterpriseSeniorityDate: EnterpriseSeniorityDate;
    OnMilitaryServiceFlag: boolean;
    WorkerNumber: WorkerNumber;
    ReadyToConvertFlag: ReadyToConvertFlag;
    TerminationDate: TerminationDate;
    NotificationDate: NotificationDate;
    LastWorkingDate: LastWorkingDate;
    RevokeUserAccess: RevokeUserAccess;
    RecommendedForRehire: string;
    RecommendationReason: RecommendationReason;
    RecommendationAuthorizedByPersonId: RecommendationAuthorizedByPersonId;
    CreatedBy: string;
    CreationDate: string;
    LastUpdatedBy: string;
    LastUpdateDate: string;
    assignments: assignments;
}

export interface assignments {
    items: itemsItem1[];
}

export interface itemsItem1 {
    AssignmentId: number;
    AssignmentNumber: string;
    AssignmentName: string;
    ActionCode: string;
    ReasonCode: ReasonCode;
    EffectiveStartDate: string;
    EffectiveEndDate: string;
    EffectiveSequence: number;
    EffectiveLatestChange: string;
    BusinessUnitId: number;
    BusinessUnitName: string;
    AssignmentType: string;
    AssignmentStatusTypeId: number;
    AssignmentStatusTypeCode: string;
    AssignmentStatusType: string;
    SystemPersonType: string;
    UserPersonTypeId: number;
    UserPersonType: string;
    ProposedUserPersonTypeId: ProposedUserPersonTypeId;
    ProposedUserPersonType: ProposedUserPersonType;
    ProjectedStartDate: ProjectedStartDate;
    ProjectedEndDate: ProjectedEndDate;
    PrimaryFlag: boolean;
    PrimaryAssignmentFlag: boolean;
    PositionId: PositionId;
    PositionCode: PositionCode;
    SynchronizeFromPositionFlag: boolean;
    JobId: JobId;
    JobCode: JobCode;
    GradeId: GradeId;
    GradeCode: GradeCode;
    GradeLadderId: GradeLadderId;
    GradeLadderName: GradeLadderName;
    GradeStepEligibilityFlag: boolean;
    GradeCeilingStepId: GradeCeilingStepId;
    GradeCeilingStep: GradeCeilingStep;
    DepartmentId: DepartmentId;
    DepartmentName: DepartmentName;
    ReportingEstablishmentId: ReportingEstablishmentId;
    ReportingEstablishmentName: ReportingEstablishmentName;
    LocationId: LocationId;
    LocationCode: LocationCode;
    WorkAtHomeFlag: boolean;
    AssignmentCategory: AssignmentCategory;
    WorkerCategory: WorkerCategory;
    PermanentTemporary: PermanentTemporary;
    FullPartTime: FullPartTime;
    ManagerFlag: boolean;
    HourlySalariedCode: HourlySalariedCode;
    NormalHours: NormalHours;
    Frequency: Frequency;
    StartTime: StartTime;
    EndTime: EndTime;
    SeniorityBasis: string;
    ProbationPeriod: ProbationPeriod;
    ProbationPeriodUnit: ProbationPeriodUnit;
    ProbationEndDate: ProbationEndDate;
    NoticePeriod: NoticePeriod;
    NoticePeriodUOM: NoticePeriodUOM;
    WorkTaxAddressId: WorkTaxAddressId;
    ExpenseCheckSendToAddress: ExpenseCheckSendToAddress;
    RetirementAge: RetirementAge;
    RetirementDate: RetirementDate;
    LabourUnionMemberFlag: LabourUnionMemberFlag;
    UnionId: UnionId;
    UnionName: UnionName;
    BargainingUnitCode: BargainingUnitCode;
    CollectiveAgreementId: CollectiveAgreementId;
    CollectiveAgreementName: CollectiveAgreementName;
    InternalBuilding: InternalBuilding;
    InternalFloor: InternalFloor;
    InternalOfficeNumber: InternalOfficeNumber;
    InternalMailstop: InternalMailstop;
    DefaultExpenseAccount: DefaultExpenseAccount;
    PeopleGroup: PeopleGroup;
    CreatedBy: string;
    CreationDate: string;
    LastUpdatedBy: string;
    LastUpdateDate: string;
}
